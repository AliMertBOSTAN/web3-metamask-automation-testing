import time
import playwright
import test
from playwright.sync_api import sync_playwright, expect
from playwright.sync_api import Page
import os

Password =  os.environ["PASSWORD"]
path_to_extension = "/Users/alimertbostan/Library/Application Support/Google/Chrome/Profile 1/Extensions/nkbihfbeogaeaoehlefnkodbefgpgknn/11.0.0_0"
user_data_dir = "/Users/alimertbostan/Library/Application Support/Google/Chrome/Profile 1/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"
# -------------------- TRANSACTION TESTS-----------------------------------
def test_CrocSwap_200_SwapTradePage(playwright):
    # ---------------------------------------------------------------------- WALLET CONNECTION--------------------------------------------------------------------------------------------
    context = playwright.chromium.launch_persistent_context(
        user_data_dir,
        headless=False,
        args=[
        f"--disable-extensions-except={path_to_extension}",
        f"--load-extension={path_to_extension}",
        ],
    )
    page = context.new_page()
    with context.expect_page() as new_page_info:
        page.goto(
            "https://ambient-proven-test.netlify.app/trade/market/chain=0x5&tokenA=0x0000000000000000000000000000000000000000&tokenB=0xD87Ba7A50B2E7E660f678A895E4B72E7CB4CCd9C",
        )
    all_pages = context.pages
    all_pages[0].close()

    meta_page = new_page_info.value
    meta_page.locator("#password").fill(Password)
    meta_page.locator(
        "#app-content > div > div.mm-box.main-container-wrapper > div > div > button"
    ).click()
    try:

        page.get_by_role("button", name="Connect Wallet").nth(1).click()
        page.locator(
        "#Modal_Global > div > div > section > div > div.WalletModalWagmi_wall_buttons_container__1HMaQ > button:nth-child(1) > div"
        ).click()
    except Exception as err:
        print("already connected", err)
    # ---------------------------------------------------------------------- END of WALLET CONNECTION--------------------------------------------------------------------------------------------
    # Enter amount to swap
    page.bring_to_front()
    page.locator("#swap_sell_qty").fill("0.1")
    sell_Base = page.locator("#swap_buy_qty")
    page.locator(
        "#root > div.Common__FlexContainer-sc-f2isqu-1.kuPnCj.content-container-trade > section > section > div.Common__FlexContainer-sc-f2isqu-1.cpDxTc > section > section > section > div > div.Common__FlexContainer-sc-f2isqu-1.hLfebe > button"
    ).click()
    # site içi pop-up onaylama
    page.locator(
        "#Modal_Global > div > div > section > div > footer > button"
    ).click()
    # ----------------------------------------------------------------------------- WALLET İŞLEM ONAYI -----------------------------------------------------------------------------------------------
    time.sleep(2)
    # metamask bekleyen işleme tıklama (unapproved button)
    meta_page.locator(
        "#app-content > div > div.mm-box.main-container-wrapper > div > div > div > div.mm-box > div > div > div > div > div.transaction-list__pending-transactions > div.list-item.transaction-list-item.transaction-list-item--unconfirmed > div.list-item__subheading > h3 > div.transaction-status-label.transaction-status-label--unapproved.transaction-status-label--unapproved"
    ).click()

    time.sleep(3)
    # metamask işlem onaylama
    meta_page.locator(
        "#app-content > div > div > div > div.confirm-page-container-content > div.page-container__footer > footer > button.button.btn--rounded.btn-primary.page-container__footer-button"
    ).click()
    # ----------------------------------------------------------------------------- End of WALLET İŞLEM ONAYI -----------------------------------------------------------------------------------------------
    time.sleep(3)
    var_CheckConfirm = page.text_content(
        "//html/body/div[1]/div[5]/div/aside/div/div/section/div/footer/div/button/div[2]")

    varBool = (var_CheckConfirm == "Transaction Submitted")
    assert varBool
    context.close()

def test_CrocSwap_205_LimitTradePage(playwright):
# ---------------------------------------------------------------------- WALLET CONNECTION--------------------------------------------------------------------------------------------
    context = playwright.chromium.launch_persistent_context(
        user_data_dir,
        headless=False,
        args=[
        f"--disable-extensions-except={path_to_extension}",
        f"--load-extension={path_to_extension}",
        ],
    )
    page = context.new_page()
    with context.expect_page() as new_page_info:
        page.goto(
            "https://ambient-proven-test.netlify.app/trade/market/chain=0x5&tokenA=0x0000000000000000000000000000000000000000&tokenB=0xD87Ba7A50B2E7E660f678A895E4B72E7CB4CCd9C",
        )
    all_pages = context.pages
    all_pages[0].close()

    meta_page = new_page_info.value
    meta_page.locator("#password").fill("Luna160399.")
    meta_page.locator(
    "#app-content > div > div.mm-box.main-container-wrapper > div > div > button"
    ).click()
    try:
        page.get_by_role("button", name="Connect Wallet").nth(1).click()
        page.locator(
            "#Modal_Global > div > div > section > div > div.WalletModalWagmi_wall_buttons_container__1HMaQ > button:nth-child(1) > div"
        ).click()
    except Exception as err:
        print("already connected", err)
    # ---------------------------------------------------------------------- END of WALLET CONNECTION--------------------------------------------------------------------------------------------
    page.bring_to_front()
    # click on limit tab
    page.get_by_role("link", name="Limit").click()
    # reverse the token so that usdc is on top
    page.get_by_label("Reverse tokens").click()
    # enter 600 usdc
    page.locator("#limit_sell_qty").click()
    page.locator("#limit_sell_qty").fill("600")
    # increase limit by one click
    page.get_by_label("Increase limit tick.").click()
    page.locator(
        "#root > div.Common__FlexContainer-sc-f2isqu-1.kuPnCj.content-container-trade > section > section > div.Common__FlexContainer-sc-f2isqu-1.cpDxTc > section > section > section > div > div.Common__FlexContainer-sc-f2isqu-1.hLfebe > button"
    ).click()
    # site içi pop-up onaylama
    page.locator(
        "#Modal_Global > div > div > section > div > footer > button"
    ).click()
    # ----------------------------------------------------------------------------- WALLET İŞLEM ONAYI -----------------------------------------------------------------------------------------------
    time.sleep(2)
    # metamask bekleyen işleme tıklama (unapproved button)
    meta_page.locator(
        "#app-content > div > div.mm-box.main-container-wrapper > div > div > div > div.mm-box > div > div > div > div > div.transaction-list__pending-transactions > div.list-item.transaction-list-item.transaction-list-item--unconfirmed > div.list-item__subheading > h3 > div.transaction-status-label.transaction-status-label--unapproved.transaction-status-label--unapproved"
    ).click()

    time.sleep(3)
    # metamask işlem onaylama
    meta_page.locator(
        "#app-content > div > div > div > div.confirm-page-container-content > div.page-container__footer > footer > button.button.btn--rounded.btn-primary.page-container__footer-button"
    ).click()
    # ----------------------------------------------------------------------------- END of WALLET İŞLEM ONAYI -----------------------------------------------------------------------------------------------
    time.sleep(3)
    var_CheckConfirm = page.text_content(
        "//html/body/div[1]/div[5]/div/aside/div/div/section/div/footer/div/button/div[2]")

    varBool = (var_CheckConfirm == "Transaction Submitted")
    assert varBool
    context.close()